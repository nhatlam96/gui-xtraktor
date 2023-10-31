/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 6.5
import QtQuick.Controls 6.5
import NewGuiTry

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Text {
        text: qsTr("Hello NewGuiTry")
        anchors.verticalCenterOffset: 195
        anchors.horizontalCenterOffset: 16
        anchors.centerIn: parent
        font.family: Constants.font.family
    }

    Text {
        id: text1
        x: 643
        y: 339
        text: qsTr("Text")
        font.pixelSize: 12
    }

    Rectangle {
        id: rectangle
        x: 616
        y: 491
        width: 200
        height: 200
        color: "#ffffff"

        BusyIndicator {
            id: busyIndicator
            x: 70
            y: 70
        }
    }

    MouseArea {
        id: mouseArea
        x: 745
        y: 379
        width: 100
        height: 100

        Button {
            id: button
            x: 429
            y: 166
            text: qsTr("Button")
        }

        Image {
            id: myScuttler
            x: 85
            y: 8
            visible: false
            source: "images/My Scuttler.png"
            state: switch1.state
            clip: false
            layer.format: ShaderEffectSource.Alpha
            layer.mipmap: false
            layer.smooth: false
            layer.enabled: false
            fillMode: Image.PreserveAspectFit
        }
    }

    TextEdit {
        id: textEdit
        x: 947
        y: 334
        width: 80
        height: 26
        text: qsTr("Text Edit")
        font.pixelSize: 12
    }

    TextInput {
        id: textInput
        x: 1172
        y: 351
        width: 80
        height: 20
        text: qsTr("Text Input")
        font.pixelSize: 12
    }

    DelayButton {
        id: delayButton
        x: 1180
        y: 628
        text: qsTr("Delay Button")
    }

    Switch {
        id: switch1
        x: 1158
        y: 456
        text: qsTr("Switch")
    }
}
