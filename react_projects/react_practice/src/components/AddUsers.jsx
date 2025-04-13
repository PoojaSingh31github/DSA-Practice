import React from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";

const AddUsersdata = () => {
    const seletor = useSelector((state) => state.data)
    const navigate = useNavigate();
    return (
        <>
            <button onClick={() => navigate("/userdetails")}>add details</button>
            <div className="overflow-x-auto p-4">
                <table className="table-auto w-full border-collapse border border-gray-400">
                    <thead>
                        <tr className="bg-gray-200">
                            <th className="border border-gray-400 p-2">Users</th>
                            <th className="border border-gray-400 p-2">Personal Details</th>
                            <th className="border border-gray-400 p-2">Address Details</th>
                            <th className="border border-gray-400 p-2">Card Details</th>
                            <th className="border border-gray-400 p-2">Professional Details</th>
                            <th className="border border-gray-400 p-2">Education Details</th>
                        </tr>
                    </thead>
                    <tbody>
                        {seletor.map((user, index) => (
                            <tr key={index}>
                                <td className="border border-gray-400 p-2 font-bold text-center">User {index + 1}</td>
                                {["personalDetails", "addressDetails", "cardDetails", "proffesionalDetails", "educationDetails"].map((section, i) => (
                                    <td key={i} className="border border-gray-400 p-2">
                                        {Object.entries(user[section]).map(([key, value]) => (
                                            <div key={key}>
                                                <strong>{key}:</strong> {value}
                                            </div>
                                        ))}
                                    </td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </>
    )
}
export default AddUsersdata;