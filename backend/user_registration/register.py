import uuid
import validators
from flask import Blueprint, current_app, request, abort
from db_conn_manager import get_db

register = Blueprint('register', __name__)


class User:
    f_name = validators.FName()
    l_name = validators.LName()
    p_c_num = validators.PrimaryContactNumber()
    s_c_num = validators.SecondaryContactNumber()
    p_email = validators.PrimaryEmailAddress()
    s_email = validators.SecondaryEmailAddress()
    p_word = validators.Password()
    address = validators.Address()
    pincode = validators.Pincode()
    m_name = validators.MName()

    def __init__(
        self,
        req: dict
    ):
        self.req = req
        self.check_missing_keys()
        self.f_name = req['f_name']
        self.l_name = req['l_name']
        self.p_c_num = req['primary_contact_number']
        self.s_c_num = req['secondary_contact_number']
        self.p_email = req['primary_email_address']
        self.s_email = req['secondary_email_address']
        self.p_word = req['password']
        self.address = req['address']
        self.pincode = req['pincode']
        self.m_name = req.get('m_name', "")  # Optional Field
        self.db = get_db()

    def check_missing_keys(self):
        required_keys = ('f_name','l_name','primary_contact_number','secondary_contact_number',
                         'primary_email_address','secondary_email_address','password',
                         'address','pincode',)
        missing_keys = list(set(required_keys) - set(self.req))
        if len(missing_keys) > 0:
            raise AttributeError(f"Missing Keys are {missing_keys}")

    def save_user(self):
        user_id = self.db.cur.execute(
            """
            WITH new_user AS (
                INSERT INTO public."user" (
                    user_identifier,f_name,m_name,l_name,primary_contact_number,
                    primary_email,secondary_contact_number,secondary_email,
                    address,pincode
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING user_id
            )
            INSERT INTO public."security_info" (p_word,user_id)
            VALUES (%s, (SELECT user_id FROM new_user))
            RETURNING user_id
            """, 
            (   
                str(uuid.uuid4()),
                self.f_name,
                self.m_name,
                self.l_name,
                self.p_c_num,
                self.p_email,
                self.s_c_num,
                self.s_email,
                self.address,
                self.pincode,
                self.p_word,
            )
        )
        self.db.conn.commit()
        return user_id


@register.route('/register', methods=["POST"])
def register_user():
    try:
        raw_req = request.json
        current_app.logger.debug(
            f"Raw Request: {raw_req}"
        )

        user = User(
            req=raw_req
        )
        user_id = user.save_user()
        current_app.logger.info(f"User has been saved. user_id: {user_id!r}")
        del user
        return "User has been created", 200
    except Exception as exp:
        current_app.logger.exception(exp)
        abort(400, str(exp))

