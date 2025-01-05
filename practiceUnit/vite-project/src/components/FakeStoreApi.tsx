import react, { useEffect } from "react";
interface Props{

}

const FakeStoreApi : React.FC<Props> = (props)=>{
    const  fetchData = async()=>{
        try {
            const res = await fetch("https://fakestoreapi.com/products")
            const data = await res.json();
            console.log(data)
        } catch (error) {
            console.log(error)
        }
    }

    useEffect(()=>{
        fetchData();
    },[])
    
    return (
        <h1>heyyy</h1>
    )
}

export default FakeStoreApi;