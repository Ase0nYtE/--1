public class SMSNotification : INotification
{
    private string _message;
    private string _status = "Pending";

    public void PrepareMessage(string message) => _message = $"SMS: {message}";
    public void Send() => _status = "SMS sent!";
    public string GetStatus() => _status;
}