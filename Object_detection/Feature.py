import cv2
import numpy as np 

reeses = cv2.imread('../DATA/reeses_puffs.png',0)
cereal = cv2.imread('../DATA/many_cereals.jpg',0)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(reeses,None)
kp2, des2 = orb.detectAndCompute(cereal,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1,des2)

single_match = matches[0]

single_match.distance

matches = sorted(matches, key =  lambda x:x.distance)

reeses_matches = cv2.drawMatches(reeses, kp1, cereal, kp2, matches[:25], None, flags= 2)

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(reeses,None)
kp2, des2 = sift.detectAndCompute(cereal,None)

bf = cv2.BFMatcher()

matches = bf.knnMatch(des1,des2, k = 2)

good = []

for match1, match2 in matches:
    if match1.distance < 0.75 * match2.distance:
        good.append([match1])

sift_matches = cv2.drawMatchesKnn(reeses, kp1, cereal, kp2, good, None, flags=2)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches2 = flann.knnMatch(des1,des2, k = 2)

good2 = []

for match1, match2 in matches:
    if match1.distance < 0.75 * match2.distance:
        good2.append([match1])

flann_matches = cv2.drawMatchesKnn(reeses, kp1, cereal, kp2, good, None, flags=0)


cv2.imwrite('comp.jpg', reeses_matches)
cv2.imwrite('sift.jpg', sift_matches)
cv2.imwrite('flan.jpg', flann_matches)
cv2.imwrite('img.jpg',cereal)
cv2.imwrite('img2.jpg',reeses)