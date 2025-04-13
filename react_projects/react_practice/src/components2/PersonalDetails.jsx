import React from "react";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { setInput } from "../reduxToolkit/userSlice";

const PersonalDetails = () => {
    const dispatch = useDispatch();

    const [state, setState] = useState({
        name: "",
        email: "",
        profession: "",
        password: "",
        hobby: "",
    });

    const handleChange = (e) => {
        setState({ ...state, [e.target.name]: e.target.value })
        console.log(state)

    }
    const handleDispatch = () => {
        console.log("dispatchedd")
        dispatch(setInput({ type: "personalDetails", payload: state }))
    }

    return (
        <div>
            <h1 className="text-3xl font-semibold text-gray-800 my-2">personal details</h1>
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="name" placeholder="enter name" required onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="email" placeholder="enter email" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="profession" placeholder="enter profession" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="password" name="password" placeholder="enter password" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="hobby" placeholder="enter hobby" onChange={handleChange} /><br />
            <button className="rounded-2xl bg-black text-white py-2 px-4 my-3 w-1/3" onClick={handleDispatch}>next</button>


        </div>
    )
}
export default PersonalDetails;