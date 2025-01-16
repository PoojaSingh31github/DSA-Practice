import react from "react";
import { useState } from "react";
import useSelector, { useDispatch } from "react-redux";

const Counter = async () => {
    const count = useSelector((state) => state.count);
    const dispatch = useDispatch();

    return (
        <div>
            <p>
                {count}
            </p>
            <button onClick={dispatch({ type: "increment" })}>inc</button>
            <button onClick={dispatch({ type: "decrement" })}>dec</button>

        </div>
    )
}

export default Counter;
