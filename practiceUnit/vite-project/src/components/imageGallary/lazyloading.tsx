import React, { useEffect, useState } from "react";

const ImageGallary: React.FC = () => {
    const [images, setimages] = useState<any[]>([]);
    const [page, setpage] = useState<number>(1);
    const fetchimages = async () => {
        try {
            const res = await fetch(
                `https://api.unsplash.com/photos?client_id=${import.meta.env.VITE_ACCESS_KEY}&page=${page}&per_page=10`
            );
            const data = await res.json()
            console.log(data)
            setimages((prev) => [...prev, ...data])
        } catch (error) {
            console.log(error)
        }
    }
    useEffect(() => {
        fetchimages()

    }, [page]);

    const handleScroll = () => {
        console.log("Scroll Height:", document.documentElement.scrollTop);
        console.log("Window Height:", window.innerHeight);
        console.log("Offset Height:", document.documentElement.offsetHeight);

        if (window.innerHeight + document.documentElement.scrollTop >= document.documentElement.offsetHeight-10) {
            setpage((prev) => prev + 1)
        }
    }

    useEffect(() => {
        window.addEventListener("scroll", handleScroll)
            return () => window.removeEventListener("scroll", handleScroll)
    }, []);

    return (
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "10px" }}>
            {images.map((ele) => (
                    <img src={ele.urls.small} key={ele.id} alt={ele.alt_description} loading="lazy" style={{ width: "100%", borderRadius: "8px" }} />
                ))
            }
        </div>
    )
}

export default ImageGallary;
