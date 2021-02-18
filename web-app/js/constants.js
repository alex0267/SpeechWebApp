let isDev = window.location.hostname == "localhost";

let apiHost = "";
if (isDev) {
    apiHost = `${window.location.protocol}//${window.location.hostname}:8081`;
} else {
    apiHost = `${window.location.protocol}//${window.location.hostname}`;
}

export {apiHost};
