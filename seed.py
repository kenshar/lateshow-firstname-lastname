from app import app, db, Episode, Guest, Appearance

with app.app_context():
    # Clear existing data
    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()

    # Create episodes
    episode1 = Episode(date="1/11/99", number=1)
    episode2 = Episode(date="1/12/99", number=2)
    episode3 = Episode(date="1/13/99", number=3)

    # Create guests
    guest1 = Guest(name="Michael J. Fox", occupation="actor")
    guest2 = Guest(name="Sandra Bernhard", occupation="Comedian")
    guest3 = Guest(name="Tracey Ullman", occupation="comedian")
    guest4 = Guest(name="Billy Crystal", occupation="actor")

    db.session.add_all([episode1, episode2, episode3, guest1, guest2, guest3, guest4])
    db.session.commit()

    # Create appearances
    appearance1 = Appearance(rating=4, episode_id=1, guest_id=1)
    appearance2 = Appearance(rating=5, episode_id=2, guest_id=2)
    appearance3 = Appearance(rating=3, episode_id=2, guest_id=3)
    appearance4 = Appearance(rating=4, episode_id=3, guest_id=4)

    db.session.add_all([appearance1, appearance2, appearance3, appearance4])
    db.session.commit()

    print("Database seeded successfully!")
