import React from 'react'

const RegisterTruckForm = () => {
  return (
    <>
      <form action="">
        <div className='m-2'>
          <label className='mr-2' htmlFor="truck_registration_number">Truck Registration Number</label>
          <input className='border-2' type="text" id='truck_registration_number' name='truck_registration_number' placeholder=' ' required />
        </div>
        <div className='m-2'>
          <label className='mr-2' htmlFor="truck_location">Truck Location</label>
          <input className='border-2' type="text" />
        </div>
      </form>
    </>
  )
}

export default RegisterTruckForm
