from sqlalchemy.orm import Session
from config.database import Base, engine
from models.user import User
from models.role import Role
from services.auth import hash_password

# Seeder Function
def seed_database():
    # Create database tables if they don't exist
    Base.metadata.create_all(bind=engine)

    # Start a database session
    with Session(engine) as session:
        # Check if roles already exist
        if session.query(Role).count() == 0:
            roles = [
                Role(name="admin"),
                Role(name="user"),
                Role(name="manager"),
            ]
            session.add_all(roles)
            print("Roles seeded.")

        # Check if users already exist
        if session.query(User).count() == 0:
            admin_role = session.query(Role).filter(Role.name == "admin").first()
            user_role = session.query(Role).filter(Role.name == "user").first()

            users = [
                User(
                    username="admin",
                    email="admin@example.com",
                    hashed_password=hash_password("admin123"),
                    role_id=admin_role.id,
                ),
                User(
                    username="testuser",
                    email="testuser@example.com",
                    hashed_password=hash_password("password123"),
                    role_id=user_role.id,
                ),
            ]
            session.add_all(users)
            print("Users seeded.")

        # Commit changes
        session.commit()
        print("Database seeded successfully.")

# Run seeder
if __name__ == "__main__":
    seed_database()
