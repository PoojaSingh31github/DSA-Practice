import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { addQuantity, removeFromCart } from "../redux/action";

const Cart = () => {
    const selectorData = useSelector((state) => state.cart)
    const dispatch = useDispatch();
    console.log(selectorData)
    const deleteProduct = (id) => {
        dispatch(removeFromCart({ id }))
    }

    const manageQuantity = (id, bool) => {
        dispatch(addQuantity({ id: id, bool: bool }))

    }
    return (
        <>
            <div className="px-20">
                <h1 className="py-10 text-center text-3xl font-bold">Cart page</h1>
                <div className="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6">
                    {
                        selectorData && selectorData.length > 0 ? selectorData.map((product, index) => (
                            <div key={product.id} className="bg-gray-300 px-2 py-5 rounded-lg flex flex-col justify-between items-center h-[300px]">
                                <img className="w-30 h-30 object-contain mb-2" src={product.image} alt="imgs" />
                                <h2>{product.title}</h2>
                                <p>{product.price}</p>
                                <p> quantity : {product.quantity}</p>
                                <div className="flex justify-center items-center gap-[10px] my-2 ">
                                    <button className="bg-black text-white font-medium text-2xl px-5" onClick={() => manageQuantity(product.id, true)} >+</button>
                                    <button className="bg-black text-white font-medium text-2xl  px-5" onClick={() => manageQuantity(product.id, false)} disabled={product.quantity < 2}>-</button>
                                </div>
                                <button className="bg-black text-white py-1 px-3 rounded-md" onClick={() => deleteProduct(product.id)}>remove from cart</button>
                            </div>
                        )) : <div className="text-5xl font-bold col-span-4 text-center">No items in cart 🛒</div>
                    }
                </div>
            </div>
        </>
    )
}

export default Cart;