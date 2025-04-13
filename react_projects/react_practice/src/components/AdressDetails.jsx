import React from "react";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { setInput } from "../redux/action";

const AddressDetails = () => {
    const dispatch = useDispatch();

    const [state, setState] = useState({
        localAdd: "",
        city: "",
        State: "",
        country: "",
        pincode: ""

    });

    const handleChange = (e) => {
        setState({ ...state, [e.target.name]: e.target.value })
        console.log(state)

    }
    const handleDispatch = () => {
        console.log("dispatchedd")
        dispatch(setInput({ type: "addressDetails", payload: state }))
    }

    return (
        <div>
            <h1 className="text-3xl font-semibold text-gray-800 my-2">Address details</h1>
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="localAdd" placeholder="enter localAddress" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="city" placeholder="enter city" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="State" placeholder="enter State" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="country" placeholder="enter country" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="pincode" placeholder="enter pincode" onChange={handleChange} /><br />
            <button className="rounded-2xl bg-black text-white py-2 px-4 my-3 w-1/3" onClick={handleDispatch}>next</button>
        </div>
    )
}
export default AddressDetails;