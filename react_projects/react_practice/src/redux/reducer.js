import { SET_INPUT, ADD_USER_DATA, ADD_TO_CART, REMOVE_FROM_CART, ADD_QUANTITY, LOAD_CART_DATA } from "./action"

const initialValue = {

    data: [],
    currentDetails: {
        personalDetails: {},
        addressDetails: {},
        cardDetails: {},
        proffesionalDetails: {},
        educationDetails: {},
    },
    cart: []
}

export const inputReducer = (state = initialValue, action) => {
    switch (action.type) {
        case SET_INPUT:
            const updatedDetails = {
                ...state.currentDetails,
                [action.payload.type]: action.payload.payload
            }
            return {
                ...state,
                currentDetails: updatedDetails,
            }
        case ADD_USER_DATA:
            return {
                ...state,
                data: [...state.data, state.currentDetails],
                currentDetails: {
                    personalDetails: {},
                    addressDetails: {},
                    cardDetails: {},
                    proffesionalDetails: {},
                    educationDetails: {},
                }
            }
        case ADD_TO_CART:
            let checkProduct = state.cart.find((ele, index) => ele.id == action.payload.id)
            if (checkProduct) {
                return {
                    ...state,
                    cart: state.cart.map((ele, index) => ele.id === action.payload.id ? { ...ele, quantity: ele.quantity + 1 } : ele)
                }
            }
            return {
                ...state,
                cart: [...state.cart, action.payload],
            }

        case REMOVE_FROM_CART:
            return {
                ...state,
                cart: state.cart.filter((ele) => ele.id != action.payload.id)

            }
        case ADD_QUANTITY:
            return {
                ...state,
                cart: state.cart.map((ele, i) => ele.id == action.payload.id ? { ...ele, quantity: action.payload.bool ? ele.quantity + 1 : ele.quantity - 1 } : ele)
            }
        case LOAD_CART_DATA:
            return {
                ...state,
                cart: action.payload
            }
        default:
            return state;
    }

}