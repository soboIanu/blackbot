require 'bundler'
Bundler.require
require "json"

# Authenticate a session with your Service Account
session = GoogleDrive::Session.from_service_account_key("client_secret.json")

# Get the spreadsheet by its title
spreadsheet = session.spreadsheet_by_title("blackbot")
# Get the first worksheet
worksheet = spreadsheet.worksheets.first

file = File.read("userslinks.json")
data = JSON.parse(file)

i2 = 2
worksheet[1, 1] = "Chan"
worksheet[1, 2] = "Data"

data.each { |cle,valeur|
  worksheet["A#{i2}"] = cle
  worksheet["B#{i2}"] = valeur
  i2 += 1
}
worksheet.save
