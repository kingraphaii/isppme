#!/bin/bash

APP_NAME=${1}
APP_REPO=${2}
APP_BRANCH=${3}

[ "${APP_BRANCH}" ] && BRANCH="-b ${APP_BRANCH}"

mkdir -p /home/frappe/frappe-bench/sites/assets
# shellcheck disable=SC2164
cd /home/frappe/frappe-bench
echo -e "frappe\nerpnext\n${APP_NAME}" > /home/frappe/frappe-bench/sites/apps.txt

mkdir -p apps
# shellcheck disable=SC2164
cd apps
# shellcheck disable=SC2086
git clone --depth 1 https://github.com/frappe/frappe ${BRANCH}
# shellcheck disable=SC2086
git clone --depth 1 ${APP_REPO} ${BRANCH}

# shellcheck disable=SC2164
cd /home/frappe/frappe-bench/apps/frappe
yarn
yarn production
yarn install --production=true

# shellcheck disable=SC2086
mkdir -p /home/frappe/frappe-bench/sites/assets/${APP_NAME}
# shellcheck disable=SC2086
cp -R /home/frappe/frappe-bench/apps/${APP_NAME}/${APP_NAME}/public/* /home/frappe/frappe-bench/sites/assets/${APP_NAME}

echo "rsync -a --delete /var/www/html/assets/erpnext /assets" >> /rsync
echo "rsync -a --delete /var/www/html/assets/${APP_NAME} /assets" >> /rsync
chmod +x /rsync

rm /home/frappe/frappe-bench/sites/apps.txt
