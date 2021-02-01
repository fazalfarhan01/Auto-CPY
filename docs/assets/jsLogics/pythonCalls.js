eel.expose(printOnWiFiConnect)
function printOnWiFiConnect(data) {
    console.log(data);
    document.getElementById("wifiConnectResponse").innerText += data + "\n";
    onRefreshClicked();
}