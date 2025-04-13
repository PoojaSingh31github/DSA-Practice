import React, { useState } from "react";
// import { DragDropContext, Droppable, Draggable } from "react-beautiful-dnd";

export const AddTodosList = () => {
    const [list, setList] = useState({ title: "", desc: "", status: "pending" });
    const [data, setData] = useState(
        JSON.parse(sessionStorage.getItem("tododata")) || []
    );
    const [editIndex, setEditIndix] = useState(null);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setList({ ...list, [name]: value });
    };

    const handleAddtodo = () => {
        if (editIndex !== null) {
            const updatedData = [...data];
            updatedData[editIndex] = list;
            setData(updatedData);
            setEditIndix(null);
        } else {
            setData([...data, list]);
        }

        setList({ title: "", desc: "" });
    };

    sessionStorage.setItem("tododata", JSON.stringify(data));

    const handleDelete = (id) => {
        const newData = data.filter((_, i) => id !== i);
        setData(newData);
    };

    const handleEdit = (i) => {
        setList(data[i]);
        setEditIndix(i);
    };

    return (
        <div className="min-h-screen bg-gradient-to-r from-pink-200 to-pink-400 py-10 px-4 sm:px-10">
            <div className="max-w-xl mx-auto bg-white p-6 rounded-2xl shadow-lg">
                <h1 className="text-3xl font-bold text-center text-pink-800 mb-6">
                    Todo List 📝
                </h1>

                <input
                    className="w-full border-2 border-pink-500 rounded-md p-2 mb-4"
                    type="text"
                    placeholder="Enter title"
                    name="title"
                    value={list.title}
                    onChange={handleChange}
                />
                <textarea
                    className="w-full border-2 border-pink-500 rounded-md p-2 mb-4"
                    placeholder="Enter description"
                    name="desc"
                    value={list.desc}
                    onChange={handleChange}
                    rows={3}
                />
                <button
                    onClick={handleAddtodo}
                    className="w-full bg-pink-600 hover:bg-pink-700 text-white font-semibold py-2 px-4 rounded-md transition-all duration-200"
                >
                    {editIndex !== null ? "Update Todo ✏️" : "Add Todo ➕"}
                </button>
            </div>

            <h2 className="text-2xl text-center text-white mt-10 font-semibold">
                Your Todos
            </h2>

            <div className="mt-6 space-y-4 max-w-xl mx-auto">
                {data.length > 0 ? (
                    data.map((ele, i) => (
                        <div
                            key={i}
                            className="bg-white p-4 rounded-xl shadow-md border-l-4 border-pink-500"
                        >
                            <div className="flex justify-between items-start">
                                <div>
                                    <h3 className="text-lg font-bold text-gray-800">
                                        📌 {ele.title}
                                    </h3>
                                    <p className="text-gray-600">{ele.desc}</p>
                                </div>
                                <div className="flex gap-3">
                                    <button
                                        className="text-red-500 hover:text-red-700 text-xl"
                                        onClick={() => handleDelete(i)}
                                        title="Delete"
                                    >
                                        🗑️
                                    </button>
                                    <button
                                        className="text-blue-500 hover:text-blue-700 text-xl"
                                        onClick={() => handleEdit(i)}
                                        title="Edit"
                                    >
                                        ✏️
                                    </button>
                                </div>
                            </div>
                        </div>
                    ))
                ) : (
                    <p className="text-center text-white text-lg mt-4">
                        No todos yet. Add something! 😊
                    </p>
                )}
            </div>
        </div>
    );
};
