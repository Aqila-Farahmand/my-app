// Switch to the database
db = db.getSiblingDB('users');

// Insert data into the user_data table
db.user_data.insert({
  name: "Alice"
});
