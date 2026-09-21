from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Problem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="problem_user")
    title = models.CharField(max_length=200)
    description = models.TextField()
    solution = models.TextField()
    is_solved = models.BooleanField(default=False)
    location = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Problem {self.title}"

    class Meta:
        verbose_name = "Problem"
        verbose_name_plural = "Problems"
        ordering = ["-created_at"]
