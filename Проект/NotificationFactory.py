public static class NotificationFactory
{
    public static INotification CreateNotification(string channel)
    {
        return channel.ToLower() switch
        {
            "email" => new EmailNotification(),
            "sms" => new SMSNotification(),
            "push" => new PushNotification(),
            "web" => new WebNotification(),
            _ => throw new ArgumentException("Unknown channel")
        };
    }
}