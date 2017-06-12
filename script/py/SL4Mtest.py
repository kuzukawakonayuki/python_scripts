#coding: UTF-8
import android
droid = android.Android()
droid.makeToast("Hello, 日本語")
droid.dialogCreateAlert("SL4A")
items = ["Cupcake", "Donut", "Eclair", "Froyo", "Gingerbread"]
droid.dialogSetItems(items)
droid.dialogShow()
response = droid.dialogGetResponse()
droid.makeToast(items[response.result["item"]])
droid.dialogDismiss()