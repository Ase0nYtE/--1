public interface INotification
{
    void Send();
    void PrepareMessage(string message);
    string GetStatus();
}