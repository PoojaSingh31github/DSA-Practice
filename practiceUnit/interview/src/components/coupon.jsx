import react, { useState } from "react";

export const CouponValidation = ()=>{
    let porductvalue = 500
    const [coupon, setcoupon] = useState("");

    const couponCodes = [{ code: "SAVE10OFF", value: 100 , count:2}, // ₹100 off

        { code: "WELCOME2025", value: 200,count:2 }, // ₹200 off
        
        { code: "FREEDELIVERY", value: 50,count:2 }, // ₹50 off (assumed free delivery value)
        
        { code: "DISCOUNT50", value: 50 , count:2}, // ₹50 of
        ];
        
    const handlecoupon = ()=>{
        console.log(coupon)
        couponCodes.filter((c)=>{
           if( c.code===coupon){
            count
            return porductvalue -= c.value
           }
        }) 
console.log(porductvalue)
    }
    
return (
<>
<input type="text" value={coupon} onChange={(e)=>setcoupon(e.target.value)} />
<button onClick={handlecoupon}>submit</button>
</>
) 
}