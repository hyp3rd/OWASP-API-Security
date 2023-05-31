# Endpoints

A list of all the endpoints used in the `crAPI`. The list is purposely gathered from the browser inspector (learn how to dig into the code without tools before learning the tools). The endpoints are not in any particular order.

**Hint:**
Check the file `main.[hash].chunk.js`

```text
"identity/"
"workshop/"
"community/"

LOGIN: "api/auth/login",
GET_USER: "api/v2/user/dashboard",
SIGNUP: "api/auth/signup",
RESET_PASSWORD: "api/v2/user/reset-password",
FORGOT_PASSWORD: "api/auth/forget-password",
VERIFY_OTP: "api/auth/v3/check-otp",
LOGIN_TOKEN: "api/auth/v4.0/user/login-with-token",
ADD_VEHICLE: "api/v2/vehicle/add_vehicle",
GET_VEHICLES: "api/v2/vehicle/vehicles",
RESEND_MAIL: "api/v2/vehicle/resend_email",
CHANGE_EMAIL: "api/v2/user/change-email",
VERIFY_TOKEN: "api/v2/user/verify-email-token",
UPLOAD_PROFILE_PIC: "api/v2/user/pictures",
UPLOAD_VIDEO: "api/v2/user/videos",
CHANGE_VIDEO_NAME: "api/v2/user/videos/<videoId>",
REFRESH_LOCATION: "api/v2/vehicle/<carId>/location",
CONVERT_VIDEO: "api/v2/user/videos/convert_video",
CONTACT_MECHANIC: "api/merchant/contact_mechanic",
RECEIVE_REPORT: "api/mechanic/receive_report",
GET_MECHANICS: "api/mechanic",
GET_PRODUCTS: "api/shop/products",
GET_SERVICES: "api/mechanic/service_requests",
BUY_PRODUCT: "api/shop/orders",
GET_ORDERS: "api/shop/orders/all",
GET_ORDER_BY_ID: "api/shop/orders/<orderId>",
RETURN_ORDER: "api/shop/orders/return_order",
APPLY_COUPON: "api/shop/apply_coupon",
ADD_NEW_POST: "api/v2/community/posts",
GET_POSTS: "api/v2/community/posts/recent",
GET_POST_BY_ID: "api/v2/community/posts/<postId>",
ADD_COMMENT: "api/v2/community/posts/<postId>/comment",
VALIDATE_COUPON: "api/v2/coupon/validate-coupon"
```

This is a good starting point to start linking the endpoints to the features of the app and to the code's logics.

## How to get the endpoints from the code

[Here is a video showing how to get the endpoints from the code.](https://user-images.githubusercontent.com/62474964/232114961-77d6e1e3-d964-44d1-8a2d-b90c4a11568d.mp4)
