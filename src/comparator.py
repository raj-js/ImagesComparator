#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image

class Comparator():

    def __calculate(self, l_img, r_img):
        g = l_img.histogram()
        s = r_img.histogram()
        assert len(g) == len(s), "error"

        data = []

        for index in range(0, len(g)):
            if g[index] != s[index]:
                data.append(1 - abs(g[index] - s[index]) / max(g[index], s[index]))
            else:
                data.append(1)

        return sum(data) / len(g)


    def __split(self, image, part_size):
        pw, ph = part_size
        w, h = image.size

        sub_image_list = []

        assert w % pw == h % ph == 0, "error"

        for i in range(0, w, pw):
            for j in range(0, h, ph):
                sub_image = image.crop((i, j, i + pw, j + ph)).copy()
                sub_image_list.append(sub_image)

        return sub_image_list


    def compare(self, l_img_path, r_img_path, size=(256, 256), part_size=(64, 64)):
        l_img = Image.open(l_img_path)
        r_img = Image.open(r_img_path)

        l_img_rgb = l_img.resize(size).convert("RGB")
        l_img_sub = self.__split(l_img_rgb, part_size)

        r_img_rgb = r_img.resize(size).convert("RGB")
        r_img_sub = self.__split(r_img_rgb, part_size)

        sub_data = 0
        for l, r in zip(l_img_sub, r_img_sub):
            sub_data += self.__calculate(l, r)

        x = size[0] / part_size[0]
        y = size[1] / part_size[1]

        return round((sub_data / (x * y)), 6)