import React, { useState } from 'react'
import PersonalDetails from './PersonalDetails';
import AddressDetails from './AdressDetails';
import CardsDetails from './CardsDetails';
import ProffesionalDetails from './ProfesionDetails';
import EducationDetails from './EducationDetails';
import Revviewdata from './Revviewdata';

function UserDetails() {
    const [step, setStep] = useState(1);
    const renderComponent = () => {
        switch (step) {
            case 1: return <PersonalDetails />
            case 2: return <AddressDetails />
            case 3: return <CardsDetails />
            case 4: return <ProffesionalDetails />
            case 5: return <EducationDetails />
            case 6: return <Revviewdata />
            default: return null
        }
    }
    return (
        <>
            {renderComponent()}
            <div className='bg-black text-xl flex justify-between items-center'>
                <button className={`bg-white text-black py-2 px-3 m-1 ${step == 1 ? "opacity-10" : "opacity-100"} cursor-pointer`} disabled={step == 1} onClick={() => setStep(step - 1)}>prev</button>
                <button className={`bg-white text-black py-2 px-3 m-1 ${step == 6 ? "opacity-50" : "opacity-100"} cursor-pointer`} disabled={step == 6} onClick={() => setStep(step + 1)}>next</button>
            </div>
        </>
    )
}

export default UserDetails
