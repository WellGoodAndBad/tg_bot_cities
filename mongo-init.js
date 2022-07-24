db.auth('test_user', 'test_password')

db = db.getSiblingDB('test_db')

db.createUser(
        {
            user: "test_user",
            pwd: "test_password",
            roles: [
                {
                    role: "readWrite",
                    db: "test_db"
                }
            ]
        }
);