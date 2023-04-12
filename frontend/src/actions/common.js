import axiosInstance from "../utils/axiosAPI";

export const getRequest = (url, setFunc, params = {}) => {
    let body = {
        params: params
    };
    return axiosInstance.get(url, body)
        .then(response => {
            console.log(response)
            if (response.status === 200) {
                setFunc(response.data);
            }
            return response
        })
        .catch((err) => {
            return err;
        });
};
