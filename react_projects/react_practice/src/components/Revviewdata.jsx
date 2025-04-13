import React from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { ADD_USER_DATA } from "../redux/action";

const Revviewdata = () => {
    const selector = useSelector((state) => state.currentDetails);
    console.log(selector, "asdfghjkertyuioxcghjk");
    const dispatch = useDispatch();
    const navigate = useNavigate();
    return (
        <div className="min-h-screen bg-gray-100 p-6">
            <button onClick={() => { dispatch({ type: ADD_USER_DATA }); navigate("/") }}>see all users</button>
            {selector.personalDetails?.name ? (
                <div className="max-w-4xl bg-white rounded-xl shadow-md p-6 space-y-6">
                    <h1 className="text-3xl font-bold text-center text-indigo-600 mb-4">
                        Review User Details
                    </h1>
                    <section>
                        <h2 className="text-xl font-semibold text-gray-800 border-b pb-1 mb-2">
                            Personal Details
                        </h2>
                        <ul className="space-y-1 text-gray-700">
                            <li><strong>Name:</strong> {selector.personalDetails.name}</li>
                            <li><strong>Email:</strong> {selector.personalDetails.email}</li>
                            <li><strong>Profession:</strong> {selector.personalDetails.profession}</li>
                            <li><strong>Password:</strong> {selector.personalDetails.password}</li>
                            <li><strong>Hobby:</strong> {selector.personalDetails.hobby}</li>
                        </ul>
                    </section>
                    <section>
                        <h2 className="text-xl font-semibold text-gray-800 border-b pb-1 mb-2">
                            Address Details
                        </h2>
                        <ul className="space-y-1 text-gray-700">
                            <li><strong>Local Address:</strong> {selector.addressDetails.localAdd}</li>
                            <li><strong>City:</strong> {selector.addressDetails.city}</li>
                            <li><strong>State:</strong> {selector.addressDetails.state}</li>
                            <li><strong>Country:</strong> {selector.addressDetails.country}</li>
                            <li><strong>Pincode:</strong> {selector.addressDetails.pincode}</li>
                        </ul>
                    </section>
                    <section>
                        <h2 className="text-xl font-semibold text-gray-800 border-b pb-1 mb-2">
                            Card Details
                        </h2>
                        <ul className="space-y-1 text-gray-700">
                            <li><strong>Aadhaar:</strong> {selector.cardDetails.addhar}</li>
                            <li><strong>PAN:</strong> {selector.cardDetails.pan}</li>
                            <li><strong>Driving License:</strong> {selector.cardDetails.driving}</li>
                        </ul>
                    </section>
                    <section>
                        <h2 className="text-xl font-semibold text-gray-800 border-b pb-1 mb-2">
                            Professional Details
                        </h2>
                        <ul className="space-y-1 text-gray-700">
                            <li><strong>Company:</strong> {selector.proffesionalDetails.company}</li>
                            <li><strong>Package:</strong> {selector.proffesionalDetails.package}</li>
                            <li><strong>Experience:</strong> {selector.proffesionalDetails.experience}</li>
                            <li><strong>Notice Period:</strong> {selector.proffesionalDetails.notice}</li>
                            <li><strong>Position:</strong> {selector.proffesionalDetails.position}</li>
                        </ul>
                    </section>
                    <section>
                        <h2 className="text-xl font-semibold text-gray-800 border-b pb-1 mb-2">
                            Education Details
                        </h2>
                        <ul className="space-y-1 text-gray-700">
                            <li><strong>Degree:</strong> {selector.educationDetails.degree}</li>
                            <li><strong>University:</strong> {selector.educationDetails.university}</li>
                            <li><strong>Start Date:</strong> {selector.educationDetails.startdate}</li>
                            <li><strong>End Date:</strong> {selector.educationDetails.enddata}</li>
                            <li><strong>Percentage:</strong> {selector.educationDetails.percentage}</li>
                        </ul>
                    </section>
                </div>
            ) : (
                <div className="text-center text-gray-600 text-lg font-medium">
                    No details available
                </div>
            )}
        </div>
    );
};

export default Revviewdata;
