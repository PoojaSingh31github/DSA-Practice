

import React from "react";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { setInput } from "../reduxToolkit/userSlice";

const ProffesionalDetails = () => {
    const dispatch = useDispatch();

    const [state, setState] = useState({
        company: "",
        package: "",
        experience: "",
        notice: "",
        position: "",
    });

    const handleChange = (e) => {
        setState({ ...state, [e.target.name]: e.target.value })
        console.log(state)

    }
    const handleDispatch = () => {
        console.log("dispatchedd")
        dispatch(setInput({ type: "proffesionalDetails", payload: state }))
    }

    return (
        <div>
            <h1 className="text-3xl font-semibold text-gray-800 my-2">proffesional details</h1>
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="company" placeholder="enter company" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="package" placeholder="enter package" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="experience" placeholder="enter experience" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="notice" placeholder="enter notice period" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="position" placeholder="enter position" onChange={handleChange} /><br />
            <button className="rounded-2xl bg-black text-white py-2 px-4 my-3 w-1/3" onClick={handleDispatch}>next</button>


        </div>
    )
}
export default ProffesionalDetails;