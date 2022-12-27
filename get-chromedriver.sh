#!/bin/bash -e

BASE_URL='https://chromedriver.storage.googleapis.com'
LATEST_RELEASE=`wget -qO - ${BASE_URL}/LATEST_RELEASE`

# Download driver.
wget ${BASE_URL}/${LATEST_RELEASE}/chromedriver_linux64.zip
unzip chromedriver_linux64.zip -d src/
rm chromedriver_linux64.zip

# List of available drivers:
#   - chromedriver_mac64.zip
#   - chromedriver_mac_arm64.zip
#   - chromedriver_win32.zip
# echo "${BASE_URL}/index.html?path=${LATEST_RELEASE}/"
