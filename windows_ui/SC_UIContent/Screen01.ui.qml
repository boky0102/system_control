

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick
import QtQuick.Controls
import SC_UI

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Rectangle {
        id: rectangle
        x: 57
        y: 415
        width: 831
        height: 610
        color: "#ffffff"
        objectName: "bla"

        ScrollView {
            id: scrollView
            x: 0
            y: 0
            width: 837
            height: 610

            Column {
                id: column
                x: 0
                y: 0
                width: 837
                height: 610

                Repeater {
                    id: repeater
                    objectName: "logWindow"
                    Text {
                        required property string modelData
                        color: "#2d4320"
                        text: modelData
                        font.pixelSize: 20
                        topPadding: 10
                        leftPadding: 20
                        font.family: "Tahoma"
                    }
                }
            }
        }
    }

    Text {
        id: _text1
        x: 334
        y: 162
        width: 277
        height: 58
        text: qsTr("System Control")
        font.pixelSize: 40
    }
}
