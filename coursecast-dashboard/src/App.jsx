import { useMemo, useState } from "react";
import data from "./coursecast_dashboard_data.json";
import { CloudSun, Search, TrendingUp, Users, CalendarDays } from "lucide-react";
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  LineChart,
  Line
} from "recharts";
import "./App.css";

function getDemandTheme(condition) {
  switch (condition) {
    case "Near Full":
      return {
        className: "near-full",
        summary: "Enrollment pressure is intense. Seats may disappear fast."
      };
    case "High Demand":
      return {
        className: "high-demand",
        summary: "Strong student interest with above average forecasted demand."
      };
    default:
      return {
        className: "moderate-demand",
        summary: "Demand is steady with room for additional enrollment."
      };
  }
}

function buildWeeklyOutlook(selectedCourse) {
  const base = selectedCourse.forecast;
  return [
    { day: "Mon", value: Math.max(base - 6, 0) },
    { day: "Tue", value: Math.max(base - 3, 0) },
    { day: "Wed", value: base },
    { day: "Thu", value: base + 2 },
    { day: "Fri", value: base + 4 },
    { day: "Sat", value: Math.max(base - 1, 0) },
    { day: "Sun", value: Math.max(base - 3, 0) }
  ];
}

export default function App() {
  const [search, setSearch] = useState("");
  const [selectedCode, setSelectedCode] = useState(data[0]?.code || "");

  const filteredCourses = useMemo(() => {
    const q = search.toLowerCase();
    return data.filter(
      (course) =>
        course.code.toLowerCase().includes(q) ||
        course.name.toLowerCase().includes(q) ||
        course.department.toLowerCase().includes(q)
    );
  }, [search]);

  const selectedCourse = useMemo(() => {
    return data.find((course) => course.code === selectedCode) || data[0];
  }, [selectedCode]);

  if (!selectedCourse) {
    return <div className="app-shell">No course data found.</div>;
  }

  const occupancy = Math.round((selectedCourse.forecast / selectedCourse.capacity) * 100);
  const theme = getDemandTheme(selectedCourse.conditions);
  const weeklyOutlook = buildWeeklyOutlook(selectedCourse);

  return (
    <div className={`app-shell ${theme.className}`}>
      <div className="container">
        <header className="topbar">
          <div>
            <div className="brand">
  <img src="/seal-horizontal.png" alt="Xavier University Logo" className="logo"/>
  <div className="brand-text">
  </div>
</div>
            <h1>CourseCast</h1>
            <p className="subtitle">
              A weather style dashboard for course demand and enrollment forecasting.
            </p>
          </div>

          <div className="controls">
            <div className="search-box">
              <Search size={16} />
              <input
                type="text"
                placeholder="Search course, code, or department"
                value={search}
                onChange={(e) => setSearch(e.target.value)}
              />
            </div>

            <select
              value={selectedCode}
              onChange={(e) => setSelectedCode(e.target.value)}
            >
              {filteredCourses.map((course) => (
                <option key={course.code} value={course.code}>
                  {course.code} | {course.name}
                </option>
              ))}
            </select>
          </div>
        </header>

        <section className="hero-card">
          <div>
            <div className="badge-row">
              <span className="badge">{selectedCourse.conditions}</span>
              <span className="badge muted">{selectedCourse.term}</span>
            </div>

            <p className="eyebrow">Current Course</p>
            <h2>{selectedCourse.code}</h2>
            <h3>{selectedCourse.name}</h3>
            <p className="meta">
              {selectedCourse.department} | {selectedCourse.instructor} | {selectedCourse.credits} credits
            </p>
            <p className="summary">{theme.summary}</p>
          </div>

          <div className="forecast-block">
            <p className="eyebrow">Forecasted Enrollment</p>
            <div className="forecast-number">
              <span>{selectedCourse.forecast}</span>
              <small>students</small>
            </div>
            <p>Feels like {selectedCourse.trend.toLowerCase()} demand</p>
          </div>
        </section>

        <section className="stats-grid">
          <div className="stat-card">
            <Users size={18} />
            <div>
              <p>Current Enrollment</p>
              <h4>{selectedCourse.currentEnrollment}</h4>
            </div>
          </div>

          <div className="stat-card">
            <TrendingUp size={18} />
            <div>
              <p>Confidence</p>
              <h4>{selectedCourse.confidence}%</h4>
            </div>
          </div>

          <div className="stat-card">
            <CalendarDays size={18} />
            <div>
              <p>Occupancy</p>
              <h4>{occupancy}%</h4>
            </div>
          </div>
        </section>

        <section className="content-grid">
          <div className="panel">
            <h3>Enrollment Trend</h3>
            <div className="chart-wrap">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={selectedCourse.history}>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.12)" />
                  <XAxis dataKey="term" stroke="rgba(255,255,255,0.75)" />
                  <YAxis stroke="rgba(255,255,255,0.75)" />
                  <Tooltip />
                  <Area
                    type="monotone"
                    dataKey="enrollment"
                    stroke="#7dd3fc"
                    fill="#7dd3fc"
                    fillOpacity={0.25}
                    strokeWidth={3}
                  />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </div>

          <div className="panel">
            <h3>7 Day Outlook</h3>
            <div className="outlook-list">
              {weeklyOutlook.map((item) => (
                <div key={item.day} className="outlook-item">
                  <div className="outlook-left">
                    <CloudSun size={16} />
                    <span>{item.day}</span>
                  </div>
                  <span>{item.value} expected seats</span>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="panel">
          <h3>Forecast Radar</h3>
          <div className="chart-wrap small">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={data.map((course) => ({ code: course.code, forecast: course.forecast }))}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.12)" />
                <XAxis dataKey="code" stroke="rgba(255,255,255,0.75)" />
                <YAxis stroke="rgba(255,255,255,0.75)" />
                <Tooltip />
                <Line type="monotone" dataKey="forecast" stroke="#7dd3fc" strokeWidth={3} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </section>
      </div>
    </div>
  );
}