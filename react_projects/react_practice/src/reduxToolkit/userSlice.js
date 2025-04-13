import { createSlice } from "@reduxjs/toolkit";

const initialState = {
    data: [],
    currentDetails: {
        personalDetails: {},
        addressDetails: {},
        cardDetails: {},
        proffesionalDetails: {},
        educationDetails: {},
    }
}

const userSlice = createSlice({
    name: "user",
    initialState,
    reducers: {
        setInput: (state, action) => {
            console.log("heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
            const { type, payload } = action.payload;
            state.currentDetails[type] = payload
        },
        addUserData: (state) => {
            state.data.push(state.currentDetails);
            state.currentDetails = {
                personalDetails: {},
                addressDetails: {},
                cardDetails: {},
                proffesionalDetails: {},
                educationDetails: {},
            }
        }
    }
})

export const { setInput, addUserData } = userSlice.actions;
export default userSlice.reducer;