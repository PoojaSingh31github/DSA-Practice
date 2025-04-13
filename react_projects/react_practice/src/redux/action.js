export const SET_INPUT = "SET_INPUT";
export const ADD_USER_DATA = "ADD_USER_DATA";
export const ADD_TO_CART = "ADD_TO_CART";
export const REMOVE_FROM_CART = "REMOVE_FROM_CART";
export const ADD_QUANTITY = "ADD_QUANTITY";
export const LOAD_CART_DATA = "LOAD_CART_DATA";

export const setInput = (value) => {
    return {
        type: SET_INPUT,
        payload: value
    }
}
export const addUserData = () => {
    return {
        type: ADD_USER_DATA,
    }
}

export const addToCart = (products) => {
    return {
        type: ADD_TO_CART,
        payload: products
    }
}
export const removeFromCart = (productID) => {
    return {
        type: REMOVE_FROM_CART,
        payload: productID
    }
}
export const addQuantity = (payload) => {
    return {
        type: ADD_QUANTITY,
        payload: payload
    }
}
export const loadCartData = (payload) => {
    return {
        type: LOAD_CART_DATA,
        payload: payload
    }
}