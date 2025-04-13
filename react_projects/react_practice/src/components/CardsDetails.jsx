import React from "react";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { setInput } from "../redux/action";

const CardsDetails = () => {
    const dispatch = useDispatch();

    const [state, setState] = useState({
        addhar: "",
        pan: "",
        driving: "",
    });

    const handleChange = (e) => {
        setState({ ...state, [e.target.name]: e.target.value })
        console.log(state)

    }
    const handleDispatch = () => {
        console.log("dispatchedd")
        dispatch(setInput({ type: "cardDetails", payload: state }))
    }

    return (
        <div>
            <h1 className="text-3xl font-semibold text-gray-800 my-2">Cards details</h1>
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="addhar" placeholder="enter addhar card" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="pan" placeholder="enter pan card" onChange={handleChange} /><br />
            <input className="px-2 py-1 border-[1px] border-black my-2" type="text" name="driving" placeholder="enter driving card" onChange={handleChange} /><br />
            <button className="rounded-2xl bg-black text-white py-2 px-4 my-3 w-1/3" onClick={handleDispatch}>next</button>


        </div>
    )
}
export default CardsDetails;