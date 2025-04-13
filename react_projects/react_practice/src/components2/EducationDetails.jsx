import React from "react";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { setInput } from "../reduxToolkit/userSlice";

const EducationDetails = () => {
    const dispatch = useDispatch();

    const [state, setState] = useState({
        degree: "",
        university: "",
        startdate: "",
        enddata: "",
        percentage: "",
    });

    const handleChange = (e) => {
        setState({ ...state, [e.target.name]: e.target.value })
        console.log(state)

    }
    const handleDispatch = () => {
        console.log("dispatchedd")
        dispatch(setInput({ type: "educationDetails", payload: state }))
    }

    return (
        <div>
            <h1 className="text-3xl font-semibold text-gray-800 my-2">Education details</h1>
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="degree" placeholder="enter degree" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="university" placeholder="enter university" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="date" name="startdate" placeholder="enter startdate" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="date" name="enddata" placeholder="enter enddata" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="percentage" placeholder="enter percentage" onChange={handleChange} /><br />
            <button className="rounded-2xl bg-black text-white py-2 px-4 my-3 w-1/3" onClick={handleDispatch}>next</button>
        </div>
    )
}
export default EducationDetails;