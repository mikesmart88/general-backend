
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .mailservice import send_mail

class SendEmail(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        company_name = request.data.get("company")
        header = request.data.get("title")
        phase = request.data.get("phase")
        email = request.data.get('email')

        print(phase)

        if not phase and email:
            return Response(
                {"error": "phase, and email are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Example: do something (send email, save, etc.)
        send_mail(email, f"<p>{phase}</p>", f"{header}", "Flare Network", f"{company_name}")

        return Response(
            {"success": "Email request received"},
            status=status.HTTP_200_OK
        )