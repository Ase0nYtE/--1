public class EmailNotification : INotification
{
    private string _message;
    private string _status = "Pending";

    public void PrepareMessage(string message) => _message = $"Email Body: {message}";
    public void Send() => _status = "Email sent successfully!";
    public string GetStatus() => _status;
}