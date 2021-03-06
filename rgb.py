import cv2
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtGui


class rgb(QWidget):

    def __init__(self, parent=None, thread=None):
        super(rgb, self).__init__(parent)
        loadUi('rgb.ui', self)
        self.parent = parent
        self.thread = thread

        # 사진파일 읽기
        imgBGR = cv2.imread('lake_louise.jpg')
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

        B, G, R = cv2.split(imgBGR)

        zeros = np.zeros((imgBGR.shape[0], imgBGR.shape[1]), np.uint8)

        imgR = cv2.merge((R, zeros, zeros))
        imgG = cv2.merge((zeros, G, zeros))
        imgB = cv2.merge((zeros, zeros, B))
        imgRG = cv2.merge((R, G, zeros))
        imgRB = cv2.merge((R, zeros, B))
        imgGB = cv2.merge((zeros, G, B))

        h, w, c = imgRGB.shape

        qimg = QtGui.QImage(imgRGB.data, w, h, w*c, QtGui.QImage.Format_RGB888).scaled(640, 480, Qt.KeepAspectRatio)
        Rimg = QtGui.QImage(imgR.data, w, h, w * c, QtGui.QImage.Format_RGB888).scaled(640, 480, Qt.KeepAspectRatio)
        Gimg = QtGui.QImage(imgG.data, w, h, w * c, QtGui.QImage.Format_RGB888).scaled(640, 480, Qt.KeepAspectRatio)
        Bimg = QtGui.QImage(imgB.data, w, h, w*c, QtGui.QImage.Format_RGB888).scaled(640, 480, Qt.KeepAspectRatio)
        RGimg = QtGui.QImage(imgRG.data, w, h, w * c, QtGui.QImage.Format_RGB888).scaled(640, 480, Qt.KeepAspectRatio)
        RBimg = QtGui.QImage(imgRB.data, w, h, w * c, QtGui.QImage.Format_RGB888).scaled(640, 480, Qt.KeepAspectRatio)
        GBimg = QtGui.QImage(imgGB.data, w, h, w * c, QtGui.QImage.Format_RGB888).scaled(640, 480, Qt.KeepAspectRatio)

        self.originCam.setPixmap(QPixmap.fromImage(qimg).scaled(self.originCam.size(), Qt.KeepAspectRatio))
        self.lbR.setPixmap(QPixmap.fromImage(Rimg).scaled(self.lbR.size(), Qt.KeepAspectRatio))
        self.lbG.setPixmap(QPixmap.fromImage(Gimg).scaled(self.lbG.size(), Qt.KeepAspectRatio))
        self.lbB.setPixmap(QPixmap.fromImage(Bimg).scaled(self.lbR.size(), Qt.KeepAspectRatio))
        self.lbRG.setPixmap(QPixmap.fromImage(RGimg).scaled(self.lbRG.size(), Qt.KeepAspectRatio))
        self.lbRB.setPixmap(QPixmap.fromImage(RBimg).scaled(self.lbRB.size(), Qt.KeepAspectRatio))
        self.lbGB.setPixmap(QPixmap.fromImage(GBimg).scaled(self.lbGB.size(), Qt.KeepAspectRatio))