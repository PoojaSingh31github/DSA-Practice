import React, { useState } from "react";

const CheckedTable = () => {
    const [isChecked, setIsChecked] = useState(Array(5).fill().map(() => Array(4).fill(false)));

    const handleChangeCheckbox = (index, index2) => {
        const updated = [...isChecked];
        console.log(updated)
        updated[index][index2] = !updated[index][index2]
        setIsChecked(updated)

    }
    return (
        <div className="bg-black p-10">
            <div className="w-2/3 flex justify-between gap-10 mx-auto rounded-lg bg-pink-400">
                <div className="w-1/3 mx-auto">
                    <h1 className="text-3xl font-semibold text-center my-6">check box </h1>
                    {
                        isChecked.map((items, index) => (
                            <div key={index} className="my-3 p-4 border-[1px] border-gray-400 ">
                                <h1 className="font-semibold text-[20px]">Teacher{index + 1}</h1>
                                {
                                    items.map((items, index2) => (
                                        <div key={index2} className="flex justify-center items-center gap-2 ">
                                            <input type="checkbox" onClick={() => handleChangeCheckbox(index, index2)} /> <p className="text-[15px]"> student{index2 + 1}</p>
                                        </div>
                                    ))
                                }
                            </div>
                        ))
                    }
                </div>


                <div className="w-1/3 mx-auto">
                    <h1 className="text-3xl font-semibold text-center my-6"> resultant check box </h1>
                    {
                        isChecked.map((student, index) => {
                            const selected = student.map((ischeck, index2) => ischeck ? index2 : null).filter(i => i != null)
                            if (selected.length == 0) return null;

                            return (
                                <>
                                    <div key={index} className=" my-3 p-4 border-[1px] border-gray-400 ">
                                        <h1 className="font-semibold text-[20px]">• Teacher {index + 1}</h1>
                                        <ul>
                                            {selected.map(studentindex => (
                                                <li key={studentindex}> Students {studentindex + 1}</li>
                                            ))
                                            }
                                        </ul>

                                    </div>
                                </>
                            )
                        })
                    }
                </div>
            </div>
        </div>
    )
}

export default CheckedTable;