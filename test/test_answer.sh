curl -i --cacert /etc/ssl/certs/ourCAbundle.crt --cert ~/.certs/my.p12 https://devel2.net.ilb.ru/deepfaq/answer -H "Content-Type: application/json" --data '{"model":"testmodel","q":"How are you?"}'