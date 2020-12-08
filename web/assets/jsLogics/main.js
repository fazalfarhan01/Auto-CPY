Devices = []

window.onload = onAppLoad();


function onAppLoad() {
    // Executes on app load
    eel.get_connected_devices()(got_devices);
}


function got_devices(devices) {
    // Callback for python get_devices()

    // This global variable if only for debugging
    Devices = devices;

    // Add devices to UI
    addDeviceToDeviceList(devices);
}


function addDeviceToDeviceList(deviceList) {
    deviceList.forEach(element => {
        var x = document.getElementById("connectedDevices");
        var option = document.createElement("option");
        option.text = element;
        option.value = element;
        x.add(option);
    });
}