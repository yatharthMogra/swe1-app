from django.db import migrations
from django.utils import timezone


def create_sample_polls(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Choice = apps.get_model("polls", "Choice")

    q1 = Question.objects.create(
        question_text="What is your favorite programming language?",
        pub_date=timezone.now(),
    )
    Choice.objects.create(question=q1, choice_text="Python", votes=0)
    Choice.objects.create(question=q1, choice_text="JavaScript", votes=0)
    Choice.objects.create(question=q1, choice_text="Java", votes=0)
    Choice.objects.create(question=q1, choice_text="C++", votes=0)

    q2 = Question.objects.create(
        question_text="What is the best web framework?",
        pub_date=timezone.now(),
    )
    Choice.objects.create(question=q2, choice_text="Django", votes=0)
    Choice.objects.create(question=q2, choice_text="Flask", votes=0)
    Choice.objects.create(question=q2, choice_text="Express.js", votes=0)
    Choice.objects.create(question=q2, choice_text="Spring Boot", votes=0)

    q3 = Question.objects.create(
        question_text="Which cloud provider do you prefer?",
        pub_date=timezone.now(),
    )
    Choice.objects.create(question=q3, choice_text="AWS", votes=0)
    Choice.objects.create(question=q3, choice_text="Azure", votes=0)
    Choice.objects.create(question=q3, choice_text="Google Cloud", votes=0)


def reverse(apps, schema_editor):
    Question = apps.get_model("polls", "Question")
    Question.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_sample_polls, reverse),
    ]
