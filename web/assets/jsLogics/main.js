Devices = []

window.onload = onAppLoad();


function onAppLoad() {
    // Executes on app load
    eel.get_connected_devices()(got_devices);
    eel.checkStartOnConnect()(setLaunchOnConnect);

    document.getElementById("recordScreen").addEventListener("change", recordingOptions);
    document.getElementById("recordFilePath").onclick = function() {
        eel.open_explorer();
    };
}

function recordingOptions() {
    if (document.getElementById("recordScreen").checked) {
        document.getElementById("recordFileOptions").style.display = "block";
        document.getElementById("fileExtensionOptions").style.display = "block";
    } else {
        document.getElementById("recordFileOptions").style.display = "none";
        document.getElementById("fileExtensionOptions").style.display = "none";
    }
}

function onRefreshClicked() {
    eel.get_connected_devices()(got_devices);
}

function changeLaunchOnConnect() {
    let status = document.getElementById("launchOnConnect").checked;
    eel.changeStartOnConnectStatus(status);
    document.getElementById("restartNotification").style.display = "block";
}


function setLaunchOnConnect(enabled) {
    if (enabled) {
        document.getElementById("launchOnConnect").checked = true;
    } else {
        document.getElementById("launchOnConnect").checked = false;
    }
    document.getElementById("launchOnConnect").addEventListener("change", changeLaunchOnConnect);
}

function got_devices(devices) {
    // Callback for python get_devices()

    // This global variable if only for debugging
    // Devices = devices;

    // Add devices to UI
    addDeviceToDeviceList(devices);
}


function addDeviceToDeviceList(deviceList) {
    // Add Connected devices to UI Dropdown
    deviceList.forEach(element => {
        if (!$(`#connectedDevices option[value='${element}']`).length > 0) {
            var x = document.getElementById("connectedDevices");
            var option = document.createElement("option");
            option.text = element;
            option.value = element;
            x.add(option);
        }
    });
}

function connectAndStart() {
    // infoFromForm = Array.from(document.querySelectorAll("#parameterForm input")).reduce((acc, input) => ({...acc, [input.id]: input.value }), {})
    // var device = document.getElementById("connectedDevices").value;
    var parameters = {
        "-s": document.getElementById("connectedDevices").value,
        "-b": document.getElementById("bitrate").value,
        "-m": document.getElementById("resolution").value,
        "--no-control": document.getElementById("wantControl").checked,
        "--turn-screen-off": document.getElementById("screenOff").checked,
        "--always-on-top": document.getElementById("alwaysOnTop").checked,
        "--fullscreen": document.getElementById("fullScreen").checked,
        "--stay-awake": document.getElementById("stayAwake").checked,
        "--record": document.getElementById("recordScreen").checked,
        "extension": document.getElementById("fileExtension").value,
    };
    console.log(`Connecting to ${parameters["-s"]}`);
    eel.start_scrcpy(parameters);
}