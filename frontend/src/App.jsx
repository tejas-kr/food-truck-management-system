import './App.css'
import RegisterTruckForm from './RegisterTrucks/RegisterTruckForm'

function App() {

  return (
    <div className='container mx-auto'>
      <nav className='p-6'>
        <h2 className='text-center text-3xl font-bold underline'>Food Truck Management System</h2>
      </nav>
      <RegisterTruckForm/>
    </div>
  )
}

export default App
