import Link from "next/link";
import Image from "next/image";
import styles from "./layout.module.css";

export default function DashboardLayout({ children }) {
  return (
    <div className={styles.container}>
      {/* Sidebar */}
      <aside className={styles.sidebar}>
        <div className={styles.logo}>
          <Link href="/dashboard">
            <Image 
              src="/logo.jpeg" 
              alt="My Logo" 
              width={60} 
              height={60} 
              className={styles.logoImage}
            />
          </Link>
        </div>

        <nav className={styles.nav}>
          <Link href="/dashboard">Dashboard</Link>
          <Link href="/dashboard/users">Users</Link>
          <Link href="/dashboard/analytics">Analytics</Link>
          <Link href="/dashboard/settings">Settings</Link>
        </nav>

        <div className={styles.footer}>© 2025 Admin Dashboard</div>
      </aside>

      {/* Main Content */}
      <main className={styles.main}>{children}</main>
    </div>
  );
}

