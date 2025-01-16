import react, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

interface Props {

}

const OneProduct: React.FC<Props> = (props) => {
    const [product, setProducts] = useState<any>(null)
    const { id } = useParams()
    const fetchData = async () => {
        if (id) {
            try {
                const res = await fetch(`https://fakestoreapi.com/products/${id}`)
                const data = await res.json();
                setProducts(data);
                console.log(data)
            } catch (error) {
                console.log(error)
            }
        }
    }

    useEffect(() => {
        if (id) {
            fetchData();
        }
    }, [id])

    return (
        <div>
            {
                product ? (<>
                            <h1>{product.title}</h1>
                        </>) :
                        
                        (<h1>
                            no porduct found
                        </h1>)

            }
        </div>
    )
}

export default OneProduct;