using Microsoft.AspNetCore.Mvc;

namespace endPoint.Controllers
{
    public class NewController1 : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
