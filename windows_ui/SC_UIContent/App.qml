// Copyright (C) 2021 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR GPL-3.0-only

import QtQuick
import SC_UI

Window {
    width: mainScreen.width
    height: mainScreen.height

    visible: true
    title: "SC_UI"

    Screen01 {
        objectName: "SCREEN"
        id: mainScreen
    }

}

