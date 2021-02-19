let isDev = window.location.hostname == "localhost" || window.location.hostname == "127.0.0.1";

let apiHost = "";
if (isDev) {
    apiHost = `${window.location.protocol}//${window.location.hostname}:8081`;
} else {
    apiHost = `${window.location.protocol}//${window.location.hostname}`;
}

export {apiHost, isDev};
